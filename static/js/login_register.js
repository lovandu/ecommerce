const loginbtn=document.querySelector('.js-login-btn');
const modalLogin=document.querySelector('.js-login-modal');
const overlayl=document.querySelector('.js-modal-overlayl');
const overlayr=document.querySelector('.js-modal-overlayr');

const registerbtn=document.querySelector('.js-register-btn');
const modalRegister=document.querySelector('.js-register-modal');

function showModal(){
    modalLogin.classList.remove('hide-modal');
}

function hideModal(){
    modalLogin.classList.add('hide-modal');
}

function showRegisterModal(){
    modalRegister.classList.remove('hide-modal');
}

function hideRegisterModal(){
    modalRegister.classList.add('hide-modal');
}


loginbtn.addEventListener('click', showModal);
overlayl.addEventListener('click', hideModal);

registerbtn.addEventListener('click', showRegisterModal);
overlayr.addEventListener('click', hideRegisterModal);

