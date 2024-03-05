import json
import requests
import aiohttp


class RadiometerService:
    def __init__(self, server_address='', token=''):
        if not server_address.endswith('/'):
            server_address += '/'
        self.__server_address = server_address
        self.__token = token
        self.__headers = {"Authorization": f'Bearer {self.__token}'}

    def get_server_address(self) -> str:
        return self.__server_address

    def get_token(self) -> str:
        return self.__token

    def set_server_address(self, server_address: str) -> None:
        if not server_address.endswith('/'):
            server_address += '/'
        self.__server_address = server_address

    def set_token(self, token: str) -> None:
        self.__token = token
        self.__headers = {"Authorization": f'Bearer {self.__token}'}

    def get_devices(self) -> list:
        devices = requests.get(f'{self.__server_address}devices', headers=self.__headers, verify=False)
        return json.loads(devices.content)

    async def get_devices_async(self) -> list:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.__server_address}devices', headers=self.__headers) as response:
                data = await response.read()
                return json.loads(data)

    def get_patients(self) -> list:
        patients = requests.get(f'{self.__server_address}patients', headers=self.__headers, verify=False)
        return json.loads(patients.content)

    async def get_patients_async(self) -> list:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.__server_address}patients', headers=self.__headers) as response:
                data = await response.read()
                return json.loads(data)

    def get_measurements(self) -> list:
        measurements = requests.get(f'{self.__server_address}measurements', headers=self.__headers, verify=False)
        return json.loads(measurements.content)

    async def get_measurements_async(self) -> list:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.__server_address}measurements', headers=self.__headers) as response:
                data = await response.read()
                return json.loads(data)

    def get_measurement(self, measurement_id: int) -> bytes:
        measurement = requests.get(f'{self.__server_address}measurements/{measurement_id}', headers=self.__headers, verify=False)
        return measurement.content

    async def get_measurement_async(self, measurement_id: int) -> bytes:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.__server_address}measurements/{measurement_id}', headers=self.__headers) as response:
                return await response.read()

    def get_calibrations(self) -> list:
        calibrations = requests.get(f'{self.__server_address}calibrations', headers=self.__headers, verify=False)
        return json.loads(calibrations.content)

    async def get_calibrations_async(self) -> list:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.__server_address}calibrations', headers=self.__headers) as response:
                data = await response.read()
                return json.loads(data)
