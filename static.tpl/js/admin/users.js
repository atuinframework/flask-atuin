// Auth - Admin Users Management
var umResetForm = function (data) {
	if (!data) {
		$('#umForm input[name=usertype]').eq(0).prop('checked', true);
		$('#inputName').val('');
		$('#inputUsername').val('');
		$('#inputPassword').val('');
		$('#inputPasswordConfirm').val('');
		$('#inputNotes').val('');
		$('#inputRole').val('ADMIN');
	}
	else {
		$('#umForm input[name=usertype][value=' + data.usertype + ']').prop('checked', true);
		$('#inputName').val(data.name);
		$('#inputUsername').val(data.username);
		$('#inputPassword').val('');
		$('#inputPasswordConfirm').val('');
		$('#inputNotes').val(data.notes);
		$('#inputRole').val(data.role);
	}
	
};

$(function () {
	$('.newUserBtn').on('click', function () {
		umResetForm();
		$('#umForm').attr('action', $(this).data('url'));
		$('#UserModal').modal('show');
	});
	
	$('.modUser').on('click', function () {
		$('#umForm').attr('action', $(this).data('url'));
		
		$.ajax(
			$(this).attr('href')
		)
		.done( function (data) {
			umResetForm(data);
			$('#UserModal').modal('show');
		});
		
		return false;
	});
	
	$('#UserModal .saveBtn').on('click', function () {
		$('#umForm').submit();
	});
});