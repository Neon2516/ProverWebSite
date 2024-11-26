let currentIndex = 0;

const items = document.querySelectorAll('.item');
const totalItems = items.length;


const nav = document.querySelector('header');
const body = document.body;



window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    nav.classList.add('sticky-nav');
    body.classList.add('sticky-nav-active');
  } else {
    nav.classList.remove('sticky-nav');
    body.classList.remove('sticky-nav-active');
  }
});

document.getElementById('next').addEventListener('click', () => {

    if (currentIndex < totalItems - 4) {
        currentIndex++;
        nextSlider();
    } else {
        document.querySelector('.btn1').style.display = `none`;
        currentIndex++;
        nextSlider();
    }
    if (currentIndex > 0) {
        document.querySelector('.btn2').style.display = `block`;
    }
});

document.getElementById('prev').addEventListener('click', () => {

    if (currentIndex > 1) {
        currentIndex--;
        prevSlider();
    } else {
        document.querySelector('.btn2').style.display = `none`;
        currentIndex--;
        prevSlider();
    }
    if (currentIndex < 2) {
        document.querySelector('.btn1').style.display = `block`;
    }
})

function nextSlider() {
    const offset = -currentIndex * 34;
    document.querySelector('.content').style.transform = `translateX(${offset}%)`;
}

function prevSlider() {
    const offset = -currentIndex * 34;
    document.querySelector('.content').style.transform = `translateX(${offset}%)`;
}




function nextSection(sectionId) {
    // Скрыть текущую секцию
    const currentSection = document.querySelector('.form-section.active');
    if (currentSection) {
        currentSection.classList.remove('active');
    }

    // Показать следующую секцию
    document.getElementById(sectionId).classList.add('active');
}









function saveButton() {
    const inputValue = document.getElementById('gos_numb').value;
    localStorage.setItem('gosNumb', inputValue); // Сохраняем значение в Local Storage
    window.location.href = 'anketa'; // Переход на другую страницу
}

function loadValue() {
    const receivedValue = localStorage.getItem('gosNumb');
    if (receivedValue) {
        document.getElementById('numberAuto').value = receivedValue; // Устанавливаем значение в поле ввода
    }
}

