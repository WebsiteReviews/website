const filterBox = document.querySelectorAll('.box');
const bookContainer = document.getElementById('bookContainer');

document.querySelector('.to-filter').addEventListener('click', event => {
    if (event.target.tagName !== 'LI') return false;

    let filterClass = event.target.dataset['f'];
    let filteredBooks = [];

    filterBox.forEach(elem => {
        elem.classList.remove('hide');
        if (!elem.classList.contains(filterClass) && filterClass!== 'all'){
            elem.classList.add('hide');
        } else {
            filteredBooks.push(elem);
        }
    });

    // Очистите контейнер перед добавлением отфильтрованных книг
    bookContainer.innerHTML = '';

    // Добавьте отфильтрованные книги в контейнер
    filteredBooks.forEach(book => {
        bookContainer.appendChild(book);
    });
});
