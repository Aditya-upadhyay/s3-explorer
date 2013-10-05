$(document).ready(function() {
   $(".toggle-sidebar").click(function() {
       if ( $("#sidebar-wrapper").hasClass("partially-hidden")){
           $("#sidebar-wrapper").removeClass("partially-hidden")
           $(".sidebar-nav").removeClass("partially-hidden")
           $("#page-content-wrapper").removeClass("expanded-page-content")
       }
       else{
         $("#sidebar-wrapper").addClass("partially-hidden")
         $(".sidebar-nav").addClass("partially-hidden")
         $("#page-content-wrapper").addClass("expanded-page-content")
       }
   })
})

