window.onload = () => {
	const main = document.getElementsByTagName('main')[0];
	const sideMenuToggle = document.getElementById('side_menu_toggle');
	let sideMenuStatus = true;
	sideMenuToggle.addEventListener('click', () => {
		if (sideMenuStatus) {
			main.style.cssText = 'margin-left: -230px';
			sideMenuStatus = false;
		} else {
			main.style.cssText = 'margin-left: 0px';
			sideMenuStatus = true;
		}
	});
};

const todoCheckboxes = document.querySelectorAll('input[type="checkbox"]');

const changeClass = (element) => {
	const todoTitle = document.getElementById(element.id.replace('status', 'title'));
	todoTitle.classList.toggle('text-decoration-line-through');
};

const postFormData = (form) => {
	const formData = new FormData(form);
	const action = form.getAttribute('action');
	const options = {
		method: 'POST',
		body: formData,
	};
	fetch(action, options).then((e) => {
		if (e.status === 200) {
			console.log('[' + Date(Date.now()) + '] post success.');
			return;
		}
		console.log('[' + Date(Date.now()) + '] post failed.');
	});
};

todoCheckboxes.forEach((checkbox) => {
	checkbox.addEventListener('change', () => {
		const parentElement = checkbox.closest('span');
		changeClass(parentElement);

		const parentForm = checkbox.closest('form');
		postFormData(parentForm);
	});
});
