const signInBtn = document.querySelector('.signin-btn');
const signUpBtn = document.querySelector('.signup-btn');
const formBox = document.querySelector('.form-box');
const formSignup = document.querySelector('.form_signup');
const body = document.body;

formBox.classList.remove('active');

signUpBtn.addEventListener('click', function () {
    formBox.classList.add('active');
    body.classList.add('active');
    formSignup.classList.remove('hidden');
});

signInBtn.addEventListener('click', function(){
    formBox.classList.remove('active');
    body.classList.remove('active');
});