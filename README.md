# RadiometerAPI

<h2> Создание экземпляра RadiometerAPI: </h2>

`radiometer_api = RadiometerAPI(server_address: str, token: str, verify_ssl: bool, session: ClientSession | None = None)` <br />
<br />
`server_address` - адрес сервера <br />
`verify_ssl` - включить/отключить проверку ssl сертификата<br />
`token` - авторизационный токен <br />
`session` - экземпляр aiohttp.ClientSession(loop=loop) с указанным циклом событий loop <br />

# Методы RadiometerAPI

<h2> Синхронные методы: </h2>

`get_measurement(id: int)` - возвращает информацию об измерении <br />
`get_measurement_with_data(id: int)` - возвращает информацию об измерении вместе с сырыми данными <br />
`get_measurements()` - возвращает информацию об измерениях <br />
`get_measurements_with_data()` - возвращает информацию об измерениях вместе с сырыми данными <br />
`get_devices()` - возвращает устройства <br />
`get_patients()` - возвращает пациентов <br />
`get_calibrations()` - возвращает калибровки <br />

<h2> Асинхронные методы: </h2>

`get_measurement_async(id: int)` - асинхронно возвращает информацию об измерении <br />
`get_measurement_with_data_async(id: int)` - асинхронно возвращает информацию об измерении вместе с сырыми данными <br />
`get_measurements_async()` - асинхронно возвращает информацию об измерениях <br />
`get_measurements_with_data_async()` - асинхронно возвращает информацию об измерениях вместе с сырыми данными <br />
`get_devices_async()` - асинхронно возвращает устройства <br />
`get_patients_async()` - асинхронно возвращает пациентов <br />
`get_calibrations_async()` - асинхронно возвращает калибровки <br />
