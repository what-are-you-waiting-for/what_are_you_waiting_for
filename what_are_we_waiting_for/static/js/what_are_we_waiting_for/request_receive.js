//
// This is our OPAT Review model for use on the front end.
//
angular.module('opal.records').factory('RequestReceive', function(){
  return function(record){
    if(!record.requested_timestamp){
      record.requested_timestamp = moment();
    }
    if(!record.received_timestamp){
      record.received_timestamp = moment();
    }
    return record;
  }
});
