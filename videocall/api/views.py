from rest_framework.views import APIView
from videocall.models import *
from mentorapp.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  .serializers import VideoCallSessionSerializer

class VideocallView(APIView):
    def post(self, request, *args, **kwargs):
        mentor_id = self.kwargs.get('mentor_id')
        print(mentor_id, "mentor_id")
        student_id = self.kwargs.get('student_id')
        print(student_id, 'student_id')
        
        # Find the Order related to the mentor and student
        order = Order.objects.filter(mentor_id=mentor_id, student_id=student_id).first()
        if not order:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Create a VideoCallSession associated with the Order
        video_call_session = VideoCallSession.objects.create(
            order=order,
            channel_name=f"video_call_{mentor_id}_{student_id}"  # Generate a unique channel name
        )
        
        # Return a success response with the video call session details
        response_data = {
            'message': 'Video call session created successfully',
            'video_call_session_id': video_call_session.id,
            'channel_name': video_call_session.channel_name,
            'mentor_id': mentor_id,
            'student_id': student_id,
        }
        serializer = VideoCallSessionSerializer(video_call_session)
        print (serializer.data,"videocalllllllllllllllllllllllllllllllllllllllllllll")
        
        # return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({'success': True, 'message': 'videocallll successfully', 'response_data': serializer.data})
    

 
