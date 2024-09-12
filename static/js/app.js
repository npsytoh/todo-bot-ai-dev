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

todoCheckboxes.forEach((checkbox) => {
	checkbox.addEventListener('change', () => {
		const parentElement = checkbox.closest('span');
		changeClass(parentElement);

		const parentForm = checkbox.closest('form');
		postFormData(parentForm);
	});
});
