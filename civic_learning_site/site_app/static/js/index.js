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

    $("zip-submit").click(function() {
      alert("asd");
      console.log("asdf");
      console.log($("zipcode-input").val());

    });

  });
