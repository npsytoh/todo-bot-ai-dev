const itemButtons = document.querySelectorAll('.button-toggle');

itemButtons.forEach((button) => {
	button.addEventListener('click', () => {
		const lastChild = button.lastElementChild;
		lastChild.classList.toggle('icon-disable');
		lastChild.classList.toggle('icon-enable');
	});
});
