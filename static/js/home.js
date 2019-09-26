$(function() {
  $(".typed").typed({
    strings: [
      "stat abner.human<br/>" +
      "><span class='caret'>$</span> work: hardware-software interaction, computer, android<br/> ^100" +
      "><span class='caret'>$</span> hobbies: read, solo travel, blogging<br/> ^300" +
      "><span class='caret'>$</span> alias: bob <br/>" +
      "><span class='caret'>$</span> highlight:  <a href='https://focus.cathopic.com/vida-interior/a-jesus-se-llega-por-maria/'>A Jesús se llega por María</a>, <a href='/projects/lifehacks'>app with >750K installs</a><br/>" +
      "><span class='caret'>$</span> job: finance assitant at <a href='https://www.kemik.gt/'>kemik.com</a><br/> ^100"
    ],
    showCursor: true,
    cursorChar: '_',
    autoInsertCss: true,
    typeSpeed: 0.001,
    startDelay: 50,
    loop: false,
    showCursor: false,
    onStart: $('.message form').hide(),
    onStop: $('.message form').show(),
    onTypingResumed: $('.message form').hide(),
    onTypingPaused: $('.message form').show(),
    onComplete: $('.message form').show(),
    onStringTyped: function(pos, self) {$('.message form').show();},
  });
  $('.message form').hide()
});