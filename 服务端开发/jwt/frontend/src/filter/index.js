import moment from "moment";


export let utc2local = function (value, simple = false) {
  //noinspection JSUnresolvedFunction
  if (moment(value).isValid()) {
    // let date = moment(value).add(-8, "hours");
    let date = moment(value);
    let date_str = date.format("YYYY-MM-DD");
    let date_hm_str = date.format("HH:mm");
    if (simple) {
      return `${date_str}`;
    } else {
      return `${date_str} ${date_hm_str}`;
    }
  }
  else {
    return value;
  }
};

