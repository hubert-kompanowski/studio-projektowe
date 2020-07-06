function create_form(){
  var form = FormApp.openById('1LKeWsNygmLpTSXoHhkg9JHjSP7Yeqm7FtivuqMZ_LOc');
  form.setAcceptingResponses(false)
  length = form.getItems().length
  for(var i = 0; i < length; i++) {
  form.deleteItem(0)
  }
  form.deleteAllResponses();
  form.setTitle("Zapisy do grup")
  var item = form.addTextItem().setTitle("Imię i Nazwisko")
  item = form.addTextItem().setTitle("Numer indeksu")
  var textValidation = FormApp.createTextValidation().requireNumber().setHelpText('Podaj poprawny numer indeksu').build();
  item.setValidation(textValidation)
}

function add_questions(courses){
  var form = FormApp.openById('1LKeWsNygmLpTSXoHhkg9JHjSP7Yeqm7FtivuqMZ_LOc');
  for(var i = 0; i<courses.length; i++){
    var item = form.addMultipleChoiceItem();
    item.setTitle(courses[i][0]);
    choices = []
    for(var j = 1; j<courses[i].length; j++){
      choices.push(item.createChoice(courses[i][j]))
    }
    item.setChoices(choices);
    item.showOtherOption(false);
  }
  form.setAcceptingResponses(true)
}

function get_answers(){
  var form = FormApp.openById('1LKeWsNygmLpTSXoHhkg9JHjSP7Yeqm7FtivuqMZ_LOc');
  form.setAcceptingResponses(false)
  var formResponses = form.getResponses();
  var result = []
  for (var i = 0; i < formResponses.length; i++) {
    var answers = {}
    var formResponse = formResponses[i];
    var itemResponses = formResponse.getItemResponses();
    for (var j = 0; j < itemResponses.length; j++) {
      var itemResponse = itemResponses[j];
      answers[itemResponse.getItem().getTitle()] = itemResponse.getResponse()
    }
    result.push(answers)
}
  return result
}