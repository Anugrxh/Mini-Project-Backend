from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import SignupSerializer, LoginSerializer
import cv2
import numpy as np
import tempfile
import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tensorflow.keras.models import load_model
from .serializers import VideoUploadSerializer






# Load model once at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'fer2013_model.h5')
model = load_model(MODEL_PATH)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


# Signup View
class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]


# Login View (only access token)
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Create access token
        access = AccessToken.for_user(user)

        return Response({
            'message': 'Login successful!',
            'access': str(access),
        })


# Logout View (optional for single token use)
class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)






class VideoEmotionAnalysisView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = VideoUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        video_file = serializer.validated_data['video']

        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            for chunk in video_file.chunks():
                temp_video.write(chunk)
            temp_path = temp_video.name

        cap = cv2.VideoCapture(temp_path)
        emotion_counts = {label: 0 for label in emotion_labels}
        total_frames = 0
        frame_skip = 3  # Process every 3rd frame for speed
        frame_index = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_index += 1
            if frame_index % frame_skip != 0:
                continue

            total_frames += 1

            # Resize for faster processing
            frame = cv2.resize(frame, (640, int(frame.shape[0] * (640 / frame.shape[1]))))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                face = gray[y:y + h, x:x + w]
                face = cv2.resize(face, (48, 48))
                face = face.astype('float32') / 255.0
                face = np.expand_dims(face, axis=0)
                face = np.expand_dims(face, axis=-1)

                prediction = model.predict(face, verbose=0)
                emotion = emotion_labels[np.argmax(prediction)]
                emotion_counts[emotion] += 1

        cap.release()
        os.remove(temp_path)

        dominant_emotion = max(emotion_counts, key=emotion_counts.get)
        summary = self.generate_summary(emotion_counts, dominant_emotion, total_frames)

        return Response({
            "emotion_counts": emotion_counts,
            "dominant_emotion": dominant_emotion,
            "summary": summary
        })

    def generate_summary(self, counts, dominant, total_frames):
        summary = f"In your video, the dominant emotion detected was {dominant}."

        if dominant == "Happy":
            summary += "You appeared confident and positive during the interview."
        elif dominant == "Sad":
            summary += "You seemed a bit low in energy. Try smiling more to project positivity."
        elif dominant == "Fear":
            summary += "You appeared nervous in several moments. Practice to improve confidence."
        elif dominant == "Neutral":
            summary += "You maintained a neutral expression most of the time, which is fine but try showing more enthusiasm."
        elif dominant == "Angry":
            summary += "You appeared tense. Consider relaxing facial muscles for a calmer appearance."
        elif dominant == "Surprise":
            summary += "You showed surprise often, perhaps due to unexpected questions."
        elif dominant == "Disgust":
            summary += "You displayed some discomfort. Try to keep a professional demeanor."

        summary += f"\n\nTotal frames analyzed: {total_frames}"
        return summary




from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_framework.response import Response

class CustomGoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

    def get_serializer(self, *args, **kwargs):
        data = self.request.data.copy()
        # print("Google Social Login request data:", data)
        if "access" in data:
            data["access_token"] = data.pop("access")
        elif "id_token" in data:
            data["id_token"] = data["id_token"]
        kwargs["data"] = data
        return super().get_serializer(*args, **kwargs)

    def get_response(self):
        data = {
            "message": "Login successful!",
            "access": getattr(self.token, "access_token", str(self.token)),
        }
        return Response(data)
