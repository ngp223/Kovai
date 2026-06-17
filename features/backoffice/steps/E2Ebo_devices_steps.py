from behave import then

from features.backoffice.pages.E2Ebo_devices_page import DevicesPage_bo


@then("accedo a dispositivos")
def step_open_devices(context):

    context.devices_page = DevicesPage_bo(
        context.driver
    )

    context.devices_page.open_devices()


@then("veo el dispositivo general")
def step_check_first_device(context):

    assert context.devices_page.device_exists(
        "android-1780998092033-u3ibhdx0f"
    )


@then("filtro por Tamus Rooftop Sevilla")
def step_filter_restaurant(context):

    context.devices_page.select_restaurant(
        "Tamus Rooftop Sevilla"
    )


@then("veo el dispositivo del restaurante")
def step_check_filtered_device(context):

    assert context.devices_page.device_exists(
        "android-1775489056106-7aozil8hj"
    )


@then("vuelvo a todos los restaurantes")
def step_all_restaurants(context):

    context.devices_page.select_restaurant(
        "Todos los restaurantes"
    )


@then("vuelvo a ver el dispositivo general")
def step_check_general_again(context):

    assert context.devices_page.device_exists(
        "android-1780998092033-u3ibhdx0f"
    )