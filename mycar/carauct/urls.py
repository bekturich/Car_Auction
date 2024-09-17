from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', CarViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name= 'car_list'),
    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='car_detail'),

    path('user', UserProfileViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='user_list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update', 'delete': 'destroy'}), name='user_detail'),

    path('category', CategoryViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                                        'put': 'update', 'delete': 'destroy'}), name='category_detail'),

    path('CarMake', CarMakeViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='CarMake_list'),
    path('CarMake/<int:pk>/', CarMakeViewSet.as_view({'get': 'retrieve',
                                                     'put': 'update', 'delete': 'destroy'}), name='CarMake_detail'),

    path('model', ModelViewSet.as_view({'get': 'list',
                                        'post': 'create'}), name='model_list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='model_detail'),

    path('auction', AuctionViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='auction_list'),
    path('auction/<int:pk>/', AuctionViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='auction_detail'),

    path('bid', BidViewSet.as_view({'get': 'list',
                                    'post': 'create'}), name='bid_list'),
    path('bid/<int:pk>/', BidViewSet.as_view({'get': 'retrieve',
                                              'put': 'update', 'delete': 'destroy'}), name='bid_detail'),

    path('order', OrderViewSet.as_view({'get': 'list',
                                        'post': 'create'}), name='order_list'),
    path('order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='order_detail'),

    path('payment', PaymentViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='payment_list'),
    path('payment/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='payment_detail'),

    path('comment', CommentViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='comment_detail'),
]