//
// This is our OPAT Review model for use on the front end.
//
angular.module('opal.records').factory('RequestReceive', function(){
  return function(record){
    record.requested_timestamp = moment();
    record.received_timestamp = moment();
    return record;
  }
});
