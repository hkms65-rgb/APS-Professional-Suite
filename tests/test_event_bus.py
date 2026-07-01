from aps.platform import DomainEvent, EventBus


def test_event_bus_dispatches_event():
    bus = EventBus()
    received = []

    bus.subscribe("module.created", received.append)
    event = DomainEvent(name="module.created", payload={"name": "Enterprise Kernel"})
    bus.publish(event)

    assert received == [event]
