// Optional JS for confirm delete or other interactions
document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('form button');
    deleteButtons.forEach(btn => {
        btn.addEventListener('click', function(e){
            if(!confirm('Are you sure you want to delete?')){
                e.preventDefault();
            }
        });
    });
});
