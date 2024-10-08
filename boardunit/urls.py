from django.urls import path
from . import views

urlpatterns = [
    path("create-boardunit/", views.create_boardunit, name="create-boardunit"),
    path("review-all/", views.review_all, name="review-all"),
    path("", views.review_all, name="review-all"),
    path("review-myboardunit", views.review_myboardunit, name="review-myboardunit"),
    path(
        "edit-myboardunit/<int:boardunit_id>",
        views.edit_myboardunit,
        name="edit-myboardunit",
    ),
    path(
        "delete-myboardunit/<int:boardunit_id>",
        views.delete_myboardunit,
        name="delete-myboardunit",
    ),
    # parent_id不為None(回覆留言)
    path(
        "review-detail/<int:boardunit_id>/<int:parent_id>/",
        views.review_detail,
        name="review-detail-parent",
    ),
    # 針對發文留言
    path(
        "review-detail/<int:boardunit_id>/",
        views.review_detail,
        name="review-detail",
    ),
]
