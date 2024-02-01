from django.urls import path

from api.view.articles import ArticlesListViews, articlesdetail

from api.view.categories import CategoriesListViews, categoriesdetail

from api.view.comments import CommentsListViews, commentsdetail

from api.view.feedbacks import FeedbacksListViews, feedbacksdetail

from api.view.filter_categories import Filter_categoryListViews, filter_categoriesdetail

from api.view.filters import FiltersListViews, filtersdetail

from api.view.libraries import LibrariesListViews, librariesdetail

from api.view.pages import PagesListViews, pagesdetail

from api.view.period_filter import Period_filterListViews, period_filterdetail

from api.view.settings import SettingsListViews, settingsdetail

from api.view.sliders import SlidersListViews, slidersdetail

from api.view.sources import SourcesListViews, sourcesdetail

urlpatterns = [
    path('articles/', ArticlesListViews.as_view(), name='articles-list'),
    path('articles/<int:pk>/', articlesdetail, name='article-detail'),

    path('categories/', CategoriesListViews.as_view(), name='categories-list'),
    path('categories/<int:pk>/', categoriesdetail, name='category-detail'),

    path('comments/', CommentsListViews.as_view(), name='comments-list'),
    path('comments/<int:pk>/', commentsdetail, name='comments-detail'),

    path('feedbacks/', FeedbacksListViews.as_view(), name='feedbacks-list'),
    path('feedbacks/<int:pk>/', feedbacksdetail, name='feedbacks-detail'),

    path('filter_categories/', Filter_categoryListViews.as_view(), name='filter_categories-list'),
    path('filter_categories/<int:pk>/', filter_categoriesdetail, name='filter_categories-detail'),

    path('filters/', FiltersListViews.as_view(), name='filters-list'),
    path('filters/<int:pk>/', filtersdetail, name='filter-detail'),

    path('libraries/', LibrariesListViews.as_view(), name='libraries-list'),
    path('libraries/<int:pk>/', librariesdetail, name='libraries-detail'),

    path('pages/', PagesListViews.as_view(), name='pages-list'),
    path('pages/<int:pk>/', pagesdetail, name='pages-detail'),

    path('period_filter/', Period_filterListViews.as_view(), name='period_filter-list'),
    path('period_filter/<int:pk>/', period_filterdetail, name='period_filter-detail'),

    path('settings/', SettingsListViews.as_view(), name='settings-list'),
    path('settings/<int:pk>/', settingsdetail, name='settings-detail'),

    path('sliders/', SlidersListViews.as_view(), name='sliders-list'),
    path('sliders/<int:pk>/', slidersdetail, name='article-detail'),

    path('sources/', SourcesListViews.as_view(), name='sources-list'),
    path('sources/<int:pk>/', sourcesdetail, name='article-detail'),

]