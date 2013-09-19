// Auth - Admin Users Management
var umResetForm = function () {
	$('#umForm input[name=usertype]').eq(0).prop('checked', true);
	$('#inputName').val('');
	$('#inputUsername').val('');
	$('#inputPassword').val('');
	$('#inputPasswordConfirm').val('');
	$('#inputNotes').val('');
	$('#inputRole').val('ADMIN');
	
};

$(function () {
	$('.newUserBtn').on('click', function () {
		umResetForm();
		$('#UserModal').modal('show');
	});
});