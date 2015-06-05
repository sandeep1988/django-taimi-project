function s4(){return Math.floor((1+Math.random())*0x10000).toString(16).substring(1);};function guid(){return s4()+s4()+'-'+s4()+'-'+s4()+'-'+
s4()+'-'+s4()+s4()+s4();}
if(window.localStorage){var user_id=window.localStorage.getItem("user_id");if(!user_id){user_id=guid();window.localStorage.setItem("user_id",user_id);}}
document.getElementById('guid').value=user_id;$(document).ready(function(){$('#sortedtable').dataTable({"sDom":"<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>","bPaginate":false,"bFilter":false,"bInfo":false});$.extend($.fn.dataTableExt.oStdClasses,{"sWrapper":"dataTables_wrapper form-inline"});});$('.rmInfo').click(function(){var pid=$(this).attr('pid')
$('.message').load("/swivels/reminfo/"+pid+"/",function(){$('.message').show();$('#row_'+pid).remove();});});