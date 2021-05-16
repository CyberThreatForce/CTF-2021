("use strict");
var selectHolder, selectClass;
//Setup
$(".form__item select").each(function() {
  if (!$(this).attr("multiple")) {
    selectClass = $(this).attr("class");
    selectHolder = '<dl class="simpleSelect ' + selectClass + '">';
    selectHolder +=
      "<dt><inner>" +
      $("option", this).first().text() +
      "</inner></dt><dd><ul>";
    $("option", this).each(function() {
      selectHolder +=
        '<li data="' + $(this).val() + '">' + $(this).text() + "</li>";
    });
    selectHolder += "</ul></dd></dl>";
    $(this).after(selectHolder);
    $("." + selectClass).wrapAll('<div class="selectContainer"></div>');
  } else {
    $(this).show();
  }
});
$(".simpleSelect dd ul li").on("click", function() {
  var t = $(this);
  $(t).parents().eq(3).find("select").val($(this).attr("data"));
});

$(".simpleSelect dt").on("click", function() {
  if (
    $(this).next("dd").hasClass("open")
  ) {
    $(this).removeClass("open").next("dd").removeClass("open");
  } else {
    $(this).addClass("open").next("dd").addClass("open");
  }
});

$(".simpleSelect dd ul li").on("click", function() {
  $(this).parents().eq(1).removeClass("open");
  $(this).parents().eq(2).find("dt").removeClass("open");
  $(this).parents().eq(3).find("dt inner").text($(this).text());
});

var $form = $(".form");
var $input = $form.find("input.amount");

$input.on("keyup", function(event) {

  var selection = window.getSelection().toString();
  if (selection !== "") {
    return;
  }

  if ($.inArray(event.keyCode, [38, 40, 37, 39]) !== -1) {
    return;
  }

  var $this = $(this);
  var input = $this.val();
  var input = input.replace(/[\D\s\._\-]+/g, "");
  input = input ? parseInt(input, 10) : 0;

  $this.val(function() {
    return input === 0 ? "" : input.toLocaleString("en-US");
  });
});

;