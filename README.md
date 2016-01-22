drf-fsm-transitions
===================

Automatically hook your Django-FSM transitions up to Django REST Framework

## Installation

```bash
pip install drf-fsm-transitions
```


## Usage

When declaring your viewset, simply mix in the result of `get_viewset_transition_action_mixin`

```python
from rest_framework import viewsets
from drf_fsm_transitions.viewset_mixins import get_viewset_transition_action_mixin

from .models import Article


class ArticleViewSet(
    get_viewset_transition_action_mixin(Article),
    viewsets.ModelViewSet
):
    queryset = Article.objects.all()
```

if `Article` had 2 transitions, `delete` and `publish`, the following API calls would be set up

- `POST /api/article/1234/delete/`
- `POST /api/article/1234/publish/`

### Custom route arguments

Passing arguments to the `@detail_route` decorator can be done by specifiying
them in the `get_viewset_transition_action_mixin` method:

```python
class ArticleViewSet(
    get_viewset_transition_action_mixin(Article, permission_classes=[...]),
    viewsets.ModelViewSet
):
    queryset = Article.objects.all()
```

This will set `permission_classes` on each `@detail_route` for all transitions.
There is currrently no way to specify individual arguments for each transition.

### Saving

By default, the model instance will be saved after the transition has been successfully called. This can be disabled with the `save_after_transition` attribute

```python
class ArticleViewSet(
    get_viewset_transition_action_mixin(Article),
    viewsets.ModelViewSet
):
    queryset = Article.objects.all()
    save_after_transition = False
```
