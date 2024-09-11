window.onload = () => {
	const sideBarContent = document.getElementsByClassName('sidebar-content')[0];
	const sideBarToggle = document.getElementById('sidebar_toggle');
	sideBarToggle.addEventListener('click', () => {
		sideBarContent.classList.toggle('d-none');
	});
};

const todoCheckboxes = document.querySelectorAll('input[type="checkbox"]');

const changeClass = (element) => {
	const todoTitle = document.getElementById(element.id.replace('status', 'title'));
	todoTitle.classList.toggle('text-decoration-line-through');
};

// const postFormData = (form) => {
// 	const formData = new FormData(form);
// 	const action = form.getAttribute('action');
// 	const options = {
// 		method: 'POST',
// 		body: formData,
// 	};
// 	fetch(action, options).then((e) => {
// 		if (e.status === 200) {
// 			console.log('[' + Date(Date.now()) + '] post success.');
// 			return;
// 		}
// 		console.log('[' + Date(Date.now()) + '] post failed.');
// 	});
// };

todoCheckboxes.forEach((checkbox) => {
	checkbox.addEventListener('change', () => {
		const parentElement = checkbox.closest('span');
		changeClass(parentElement);

		const parentForm = checkbox.closest('form');
		postFormData(parentForm);
	});
});
