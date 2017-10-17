//
// This is our OPAT Review model for use on the front end.
//
angular.module('opal.records').factory('RequestReceive', function(){
  return function(record){
    if(!record.requested_timestamp){
      record.requested_timestamp = moment();
    }
    if(!record.reviewed_timestamp){
      record.reviewed_timestamp = moment();
    }
    return record;
  }
});
