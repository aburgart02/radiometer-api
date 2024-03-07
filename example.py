import asyncio
import aiohttp
from radiometer_api.radiometer_api import RadiometerAPI


def check_requests():
    measurements = radiometer_service.get_measurements()
    print(f'Measurements: {measurements}')
    measurements_with_data = radiometer_service.get_measurements_with_data()
    print(f'Measurements with data: {measurements_with_data}')

    measurement = radiometer_service.get_measurement(1)
    print(f'Measurement: {measurement}')
    measurement_with_data = radiometer_service.get_measurement_with_data(1)
    print(f'Measurement with data: {measurement_with_data}')

    devices = radiometer_service.get_devices()
    print(f'Devices: {devices}')
    patients = radiometer_service.get_patients()
    print(f'Patients: {patients}')
    calibrations = radiometer_service.get_calibrations()
    print(f'Calibrations: {calibrations}')


async def check_async_requests():
    measurements_async = await radiometer_service.get_measurements_async()
    print(f'Measurements async: {measurements_async}')
    measurement_async = await radiometer_service.get_measurement_async(1)
    print(f'Measurement async: {measurement_async}')

    measurements_with_data_async = await radiometer_service.get_measurements_with_data_async()
    print(f'Measurements with data async: {measurements_with_data_async}')
    measurement_with_data_async = await radiometer_service.get_measurement_with_data_async(1)
    print(f'Measurement with data async: {measurement_with_data_async}')

    devices_async = await radiometer_service.get_devices_async()
    print(f'Devices async: {devices_async}')
    patients_async = await radiometer_service.get_patients_async()
    print(f'Patients async: {patients_async}')
    calibrations_async = await radiometer_service.get_calibrations_async()
    print(f'Calibrations async: {calibrations_async}')

    await session.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession(loop=loop)
    radiometer_service = RadiometerAPI('https://localhost:7209/',
                                        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBcGlVc2VyIiwibmJmIjoxNzA5NzI0NDY0LCJleHAiOjE3MTUxMDg0MDAsImlzcyI6IlNlcnZlciIsImF1ZCI6IkNsaWVudCJ9.0-6FU8o7HuzrDxTAw1eytWMtjAsDudi6WT1S4CvEL3k',
                                       session)
    check_requests()
    loop.run_until_complete(check_async_requests())
