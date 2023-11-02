document.getElementById('review-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var reviewText = this.querySelector('textarea').value;
    var reviewsList = document.getElementById('reviews-list');

    var reviewElement = document.createElement('div');
    reviewElement.classList.add('review');
    reviewElement.innerHTML = reviewText;

    reviewsList.appendChild(reviewElement);

    this.reset(); // Очищаем форму
});