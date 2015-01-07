from rest_framework.decorators import detail_route
from rest_framework.response import Response


def get_transition_viewset_method(transition_name):
    '''
    Create a viewset method for the provided `transition_name`
    '''
    @detail_route(methods=['post'])
    def inner_func(self, request, pk=None):
        object = self.get_object()
        transition_method = getattr(object, transition_name)

        transition_method(by=self.request.user)

        if self.save_after_transition:
            object.save()

        serializer = self.get_serializer(object)
        return Response(serializer.data)

    return inner_func


def get_viewset_transition_action_mixin(model):
    '''
    Find all transitions defined on `model`, then create a corresponding
    viewset action method for each and apply it to `Mixin`. Finally, return
    `Mixin`
    '''
    instance = model()

    class Mixin(object):
        save_after_transition = True

    transitions = instance.get_all_status_transitions()
    transition_names = set(x.name for x in transitions)
    for transition_name in transition_names:
        setattr(
            Mixin,
            transition_name,
            get_transition_viewset_method(transition_name)
        )

    return Mixin
