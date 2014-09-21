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
from drf_transition_methods.viewset_mixins import get_viewset_transition_action_mixin

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
