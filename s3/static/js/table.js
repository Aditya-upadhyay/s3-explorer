$(document).ready(function() {
     $('.table').dataTable({
          "fnPreDrawCallback": function(oSettings, json) {
                 $('.dataTables_filter input').addClass('form-control input-sm');
                 $('.dataTables_filter input').css('width', '200px');
                 $('.dataTables_length select').addClass('form-control input-sm');
                 $('.dataTables_length select').css('width', '75px');
          }
     });
     $("#file_list_filter").children().children().attr("placeholder", "Search")
});