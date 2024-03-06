import asyncio
from radiometer_service.radiometer_service import RadiometerService

r = RadiometerService('https://localhost:7209/', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBcGlVc2VyIiwibmJmIjoxNzA5NjM2Mzk3LCJleHAiOjE3MDk3MjI3OTcsImlzcyI6IlNlcnZlciIsImF1ZCI6IkNsaWVudCJ9.j7Gb3of8h2TXY24cczOJXKPkj4dhUVj47tjcItmjcXE')

measurements = r.get_measurements()
print(f'Measurements: {measurements}')
measurements_with_data = r.get_measurements_with_data()
print(f'Measurements with data: {measurements_with_data}')

measurement = r.get_measurement(1)
print(f'Measurement: {measurement}')
measurement_with_data = r.get_measurement_with_data(1)
print(f'Measurement with data: {measurement_with_data}')

devices = r.get_devices()
print(f'Devices: {devices}')
patients = r.get_patients()
print(f'Patients: {patients}')
calibrations = r.get_calibrations()
print(f'Calibrations: {calibrations}')

measurements_async = asyncio.run(r.get_measurements_async())
print(f'Measurements async: {measurements_async}')
measurement_async = asyncio.run(r.get_measurement_async(1))
print(f'Measurement async: {measurement_async}')

measurements_with_data_async = asyncio.run(r.get_measurements_with_data_async())
print(f'Measurements with data async: {measurements_with_data_async}')
measurement_with_data_async = asyncio.run(r.get_measurement_with_data_async(1))
print(f'Measurement with data async: {measurement_with_data_async}')

devices_async = asyncio.run(r.get_devices_async())
print(f'Devices async: {devices_async}')
patients_async = asyncio.run(r.get_patients_async())
print(f'Patients async: {patients_async}')
calibrations_async = asyncio.run(r.get_calibrations_async())
print(f'Calibrations async: {calibrations_async}')
