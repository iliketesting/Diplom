# Султанова Алия, 8а когорта — Финальный проект. Инженер по тестированию плюс
import orders


def test_get_order_by_track():
    number_of_this_track = orders.create_order().json()['track']
    track_order = orders.get_order_by_track(number_of_this_track)
    assert track_order.status_code == 200;



