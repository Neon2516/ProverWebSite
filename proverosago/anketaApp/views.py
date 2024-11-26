from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarForm, DriverForm, OwnerForm, ContactsForm, CarsForm
from .models import Car, Driver, Owner, Contacts, Cars

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

from django.db import connection

# Create your views here.

driver_path = 'C:\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

drive = None


def parse1(driver):



    try:
        driver.get('https://www.sravni.ru/osago/anketa/')
        wait = WebDriverWait(driver, 60)
        time.sleep(1)

        # Автомобиль

        car = get_object_or_404(Car)
        number_auto = car.numberAuto
        firm_auto = car.firmAuto
        model_auto = car.modelAuto
        date_create = car.dateCreate
        power_engine = car.powerEngine
        series_number_sts = car.seriesNumberSTS
        date_give_doc = car.dateGiveDoc
        number_vin = car.numberVIN


        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[span[text()="Заполнить по номеру"]]')))
        button.click()
        time.sleep(1)

        carNumber = wait.until(EC.presence_of_element_located((By.NAME, 'carNumber')))
        # carNumber.send_keys('Е750ВК02')
        carNumber.send_keys(number_auto)

        carBrand = wait.until(EC.presence_of_element_located((By.NAME, 'carBrand')))
        carBrand.click()
        time.sleep(1)
        carBrand = wait.until(EC.presence_of_element_located((By.NAME, 'carBrand')))
        carBrand.click()

        carBrand.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
        carBrand.send_keys(Keys.BACKSPACE)
        # carBrand.send_keys('Suzuki')
        carBrand.send_keys(firm_auto)


        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Suzuki')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), '{firm_auto}')]"))).click()

        carModel = wait.until(EC.presence_of_element_located((By.NAME, 'carModel')))
        carModel.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
        carModel.send_keys(Keys.BACKSPACE)
        # carModel.send_keys('SX4')
        carModel.send_keys(model_auto)


        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'SX4')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), '{model_auto}')]"))).click()



        carManufactureYear = wait.until(EC.presence_of_element_located((By.NAME, 'carManufactureYear')))
        carManufactureYear.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
        carManufactureYear.send_keys(Keys.BACKSPACE)
        # carManufactureYear.send_keys('2007')
        carManufactureYear.send_keys(date_create)

        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), '2007')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), '{date_create}')]"))).click()


        enginePower = wait.until(EC.presence_of_element_located((By.NAME, 'enginePower')))
        # enginePower.send_keys('107 л.с. / 78,7 кВт')
        enginePower.send_keys(power_engine)

            # EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), '107 л.с. / 78,7 кВт')]"))).click()

        wait.until(
            EC.visibility_of_element_located((By.XPATH, f"(//div[contains(text(), '{power_engine}')])[1]"))).click()


        # Выбор типа документа (если это кастомный элемент)
        # document_type_field = wait.until(EC.element_to_be_clickable((By.NAME, 'documentType')))
        documentType = wait.until(EC.presence_of_element_located((By.NAME, 'documentType')))
        documentType.click()  # Кликаем на поле выбора

        # Ждем появления элементов выпадающего списка и выбираем нужный пункт
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'СТС')]"))).click()

        documentNumber = wait.until(EC.presence_of_element_located((By.NAME, 'documentNumber')))
        documentNumber.click()

        documentNumber.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
        documentNumber.send_keys(Keys.BACKSPACE)
        # documentNumber.send_keys('02 СК 117849')
        documentNumber.send_keys(series_number_sts)

        documentIssueDate = wait.until(EC.presence_of_element_located((By.NAME, 'documentIssueDate')))
        documentIssueDate.click()
        documentIssueDate.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
        documentIssueDate.send_keys(Keys.BACKSPACE)
        # documentIssueDate.send_keys('06.02.2008')


        formatted_date = date_give_doc.strftime("%d.%m.%Y")

        documentIssueDate.send_keys(formatted_date)

        identifyType = wait.until(EC.presence_of_element_located((By.NAME, 'identifyType')))
        identifyType.click()  # Кликаем на поле выбора

        # Ждем появления элементов выпадающего списка и выбираем нужный пункт
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'VIN номер')]"))).click()

        vinNumber = wait.until(EC.presence_of_element_located((By.NAME, 'carVinNumber')))

        vinNumber.click()
        vinNumber.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
        vinNumber.send_keys(Keys.BACKSPACE)
        # vinNumber.send_keys('TSMEYB21S00210455')
        vinNumber.send_keys(number_vin)

        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[span[text()="Продолжить"]]')))
        button.click()

        time.sleep(1)

        driverCar = get_object_or_404(Driver)

        # Создаем переменные для каждого атрибута модели Driver
        fio_driver = driverCar.fioDriver
        bith_date_driver = driverCar.bithDateDriver
        series_number_licence = driverCar.seriesNumberLicence
        date_of_start_drive = driverCar.dateOfStartDrive

        time.sleep(1)
        # Водитель
        fioDriver = wait.until(EC.presence_of_element_located((By.NAME, 'fullName')))
        fioDriver.click()
        # fioDriver.send_keys('Сычев Никита Андреевич')
        fioDriver.send_keys(fio_driver)
        time.sleep(1)
        birthdayDriver = wait.until(EC.presence_of_element_located((By.NAME, 'birthday')))
        birthdayDriver.click()
        birthdayDriver.send_keys(Keys.CONTROL + "a")
        # birthdayDriver.send_keys('18.04.2003')
        time.sleep(1)

        formatted_date = bith_date_driver.strftime("%d.%m.%Y")

        birthdayDriver.send_keys(formatted_date)
        time.sleep(1)
        licenceNumberDriver = wait.until(EC.presence_of_element_located((By.NAME, 'licenceNumber')))
        licenceNumberDriver.click()
        licenceNumberDriver.send_keys(Keys.CONTROL + "a")
        # licenceNumberDriver.send_keys('9928024565')
        licenceNumberDriver.send_keys(series_number_licence)
        time.sleep(1)
        experienceStartDateDriver = wait.until(EC.presence_of_element_located((By.NAME, 'experienceStartDate')))
        experienceStartDateDriver.send_keys(Keys.CONTROL + "a")
        # experienceStartDateDriver.click()
        # experienceStartDateDriver.send_keys('015.05.2021')

        time.sleep(1)
        formatted_date = date_of_start_drive.strftime("%d.%m.%Y")

        experienceStartDateDriver.send_keys(formatted_date)
        time.sleep(1)
        hasPreviousLicenceDriver = wait.until(EC.presence_of_element_located((By.NAME, 'hasPreviousLicence')))
        hasPreviousLicenceDriver.click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Нет')]"))).click()

        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[span[text()="Продолжить"]]')))
        button.click()

        time.sleep(1)


        # Собственник

        owner = get_object_or_404(Owner)

        # Создаем переменные для каждого атрибута модели Owner
        fio_owner = owner.fioOwner
        bith_date_owner = owner.bithDateOwner
        series_number_passport = owner.seriesNumberPassport
        date_give_passport = owner.dateGivePassport
        adrees_reg = owner.adreesReg
        number_apart = owner.numberAppart
        fio_cear_auto = owner.fioCearAuto

        time.sleep(1)

        fioOwner = wait.until(EC.presence_of_element_located((By.NAME, 'fullName')))
        fioOwner.click()
        fioOwner.send_keys(Keys.CONTROL + "a")
        # fioOwner.send_keys('Газиева Гузель Маскуровна')
        fioOwner.send_keys(fio_owner)

        birthdayOwner = wait.until(EC.presence_of_element_located((By.NAME, 'birthday')))
        birthdayOwner.click()
        birthdayOwner.send_keys(Keys.CONTROL + "a")
        # birthdayOwner.send_keys('15.06.1965')


        formatted_date = bith_date_owner.strftime("%d.%m.%Y")

        birthdayOwner.send_keys(formatted_date)
        #passportNumberOwner = driver.find_element(By.NAME, 'passportNumber')
        passportNumberOwner = wait.until(EC.presence_of_element_located((By.NAME, 'passportNumber')))
        passportNumberOwner.click()
        passportNumberOwner.send_keys(Keys.CONTROL + "a")
        # passportNumberOwner.send_keys('8010098999')
        passportNumberOwner.send_keys(series_number_passport)

        passportIssueDateOwner = wait.until(EC.presence_of_element_located((By.NAME, 'passportIssueDate')))
        passportIssueDateOwner.click()
        passportIssueDateOwner.send_keys(Keys.CONTROL + "a")

        # passportIssueDateOwner.send_keys('02.07.2010')


        formatted_date = date_give_passport.strftime("%d.%m.%Y")

        passportIssueDateOwner.send_keys(formatted_date)

        registrationAddressOwner = wait.until(EC.presence_of_element_located((By.NAME, 'registrationAddress')))
        registrationAddressOwner.click()
        registrationAddressOwner.send_keys(Keys.CONTROL + "a")
        # registrationAddressOwner.send_keys('г Уфа, ул Георгия Мушникова, д 13/2')
        registrationAddressOwner.send_keys(adrees_reg)
        wait.until(EC.visibility_of_element_located(
            # (By.XPATH, "//div[contains(text(), 'г Уфа, ул Георгия Мушникова, д 13/2')]"))).click()
            (By.XPATH, f"//div[contains(text(), '{adrees_reg}')][1]"))).click()

        registrationAddressFlatOwner = wait.until(EC.presence_of_element_located((By.NAME, 'registrationAddressFlat')))
        registrationAddressFlatOwner.click()
        registrationAddressFlatOwner.send_keys(Keys.CONTROL + "a")
        # registrationAddressFlatOwner.send_keys('184')
        registrationAddressFlatOwner.send_keys(number_apart)

        policyHolderOwner = wait.until(EC.presence_of_element_located((By.NAME, 'policyHolder')))
        policyHolderOwner.click()
        policyHolderOwner.send_keys(Keys.CONTROL + "a")
        # policyHolderOwner.send_keys(Keys.CONTROL + "a")  # Выделить весь текст
        # policyHolderOwner.send_keys(Keys.BACKSPACE)
        #
        # policyHolderOwner.send_keys('Газиева Гузель Маскуровна')
        # time.sleep(3)
        wait.until(EC.visibility_of_element_located(
            # (By.XPATH, "//div[contains(text(), 'Газиева Гузель Маскуровна')]"))).click()
            (By.XPATH, f"//div[contains(text(), '{fio_cear_auto}')]"))).click()

        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[span[text()="Продолжить"]]')))
        button.click()

        time.sleep(1)

        # Контакты

        contacts = get_object_or_404(Contacts)

        # Создаем переменные для каждого атрибута модели Contacts
        email_poch = contacts.email
        number_phone = contacts.numberPhone

        time.sleep(5)
        #email = driver.find_element(By.NAME, 'email')
        email = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
        email.click()
        email.send_keys(Keys.CONTROL + "a")
        # email.send_keys('nik04.2003@gmail.com')
        email.send_keys(email_poch)

        mobilePhone = wait.until(EC.presence_of_element_located((By.NAME, 'mobilePhone')))
        mobilePhone.click()
        mobilePhone.send_keys(Keys.CONTROL + "a")
        # mobilePhone.send_keys('9279491141')
        if(number_phone[0] == '8'):
            number_phone = number_phone[1:]
        else:
            number_phone = number_phone[2:]
        mobilePhone.send_keys(number_phone)
        time.sleep(3)
    finally:
        pass

def parse2(driver, code):
    try:
        wait = WebDriverWait(driver, 60)
        smsCode = wait.until(EC.presence_of_element_located((By.NAME, 'smsCode')))
        smsCode.click()
        smsCode.send_keys(Keys.CONTROL + "a")
        smsCode.send_keys(str(code))
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[span[text()="Применить код"]]')))
        button.click()
        time.sleep(1)
    finally:
        pass

def parsePrice(drive):

    try:
        # Откройте нужный URL
        #drive.get('https://www.sravni.ru/osago/propositions/?calculationHash=LaF_gpPmaHKt7PMXMTaZ2g')

        # Подождите, пока страница загрузится
        wait = WebDriverWait(drive, 60)

        # Найдите элементы с названиями компаний и ценами
        company_names = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'CompanyNameBlockWithSkeleton_companyName__8MYjo')))
        prices = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'Heading_module_container__7b355c09')))
        print(len(prices))
        print(len(company_names))
        prices.pop(0)
        prices.pop(0)
        prices.pop(0)
        # Извлеките текст из найденных элементов
        dict = {}
        for name, price in zip(company_names, prices):
            print(f'Компания: {name.text.strip()} - Цена: {price.text.strip()}')
            dict[name.text.strip()] = price.text.strip()

        return dict

    finally:
        # Закройте браузер
        drive.quit()


def results(request):
    global  drive
    data = {}
    some_condition = False

    # Проверяем, установлен ли флаг в сессии
    if request.session.get('can_access_results'):
        if request.method == 'POST':
            if 'calculate' in request.POST:
                some_condition = True
                code = request.POST.get('smsInput')
                parse2(drive, code)
                data = parsePrice(drive)

        return render(request, 'anketa/results.html', {'data': data, 'm1': 'hidden' if some_condition else '', 'm2': '' if some_condition else 'content2', 'm3': '' if some_condition else 'hidden'})
    else:
        # Если флаг не установлен, перенаправляем на другую страницу
        return redirect('anketa')  # Замените на нужный вам URL

def anketa(request):
    global drive

    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE anketaapp_car")
        cursor.execute("TRUNCATE TABLE anketaapp_driver")
        cursor.execute("TRUNCATE TABLE anketaapp_owner")
        cursor.execute("TRUNCATE TABLE anketaapp_contacts")

    error = {'Марка': 'Модель', 'b': 2, 'c': 3}
    if request.method == 'POST':
        if 'giveSms' in request.POST:
            car_form = CarForm(request.POST)
            driver = DriverForm(request.POST)
            owner = OwnerForm(request.POST)
            contacts = ContactsForm(request.POST)
            if car_form.is_valid() and driver.is_valid() and owner.is_valid() and contacts.is_valid():
                drive = webdriver.Chrome(service=service, options=options)

                car_form.save()
                driver.save()
                owner.save()
                contacts.save()
                parse1(drive)

                # Установим флаг в сессии
                request.session['can_access_results'] = True

                return redirect('results')
            else:
                error = 'Форма была неверной'


    car = CarForm()
    driver = DriverForm()
    owner = OwnerForm()
    contacts = ContactsForm()
    cars = CarsForm()


    data = {
        'cars': cars,
        'car': car,
        'driver': driver,
        'owner': owner,
        'contacts': contacts
    }

    return render(request, 'anketa/anketa.html', data)

def get_models(request):
    firm = request.GET.get('firm', None)
    if firm:
        models = Cars.objects.filter(Марка=firm).values_list('Модель', flat=True)
        return JsonResponse(list(models), safe=False)
    return JsonResponse([], safe=False)


