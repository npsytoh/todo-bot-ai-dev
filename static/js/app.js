window.onload = () => {
	const sideBarContent = document.getElementsByClassName('sidebar-content')[0];
	const sideBarToggle = document.getElementById('sidebar_toggle');
	sideBarToggle.addEventListener('click', () => {
		sideBarContent.classList.toggle('d-none');
	});
};
