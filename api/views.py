from rest_framework import viewsets, filters
from polls.models import Question, Choice
from .pagination import DefaultPagination
from .serializers import QuestionSerializer, ChoiceSerializer
from django.db.models import Count


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.prefetch_related('choices')
    serializer_class = QuestionSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'question_text', 'pub_date']
    search_fields = ['id', 'question_text', 'pub_date']
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = Question.objects.prefetch_related('choices')
        min_choice_count = self.request.query_params.get('min_choice_count')
        max_choice_count = self.request.query_params.get('max_choice_count')
        if max_choice_count is not None:
            queryset = queryset \
                .annotate(choice_count=Count('choices')) \
                .filter(choice_count__lte=max_choice_count)
            return queryset
        if min_choice_count is not None:
            queryset = queryset \
                .annotate(choice_count=Count('choices')) \
                .filter(choice_count__gte=min_choice_count)
        return queryset


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'choice_text', 'votes']
    search_fields = ['id', 'choice_text', 'votes']
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = Choice.objects.prefetch_related('question')
        question_text = self.request.query_params.get('question_text')
        if question_text is not None:
            queryset = queryset
        return queryset





