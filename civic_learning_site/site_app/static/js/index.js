$(document).ready(function() {
    $('#map').usmap({
      // The click action
      click: function(event, data) {
        if (data.name == 'MA') {
          $('#clicked-state')
          .text('Massachusetts, eh?');
        $('#confirm-button').show();
        }
      }
    });
  });
