import React, { Component } from 'react';
import Calendar from './calendar/Calendar';
import moment from 'moment'



export default class DisplaySelectedItem extends Component {
  constructor() {
    super();
    this.state = {
      datesSelected: ['', ''],
      notification: ['']
    }

    this.setSelectedDates = this.setSelectedDates.bind(this);

  }
  setSelectedDates = (dateArr) => {
    this.setState({
      datesSelected: dateArr
    })
  }

  formatDate = (dateArrPos) => {
    let ends = this.state.datesSelected[dateArrPos];
    let datey = new moment(ends);
    datey = datey.format();
    console.log("DATEY: ")
    console.log(datey)
    return datey;
  }


  render() {
    var Thing = this.props.ActuallySelectedItem;
    var submitFormAjax = () => {
      let payload = {
        "item": this.props.ActuallySelectedItem.id,
        "customer": "1",
        "begins": new moment(this.state.datesSelected[0]).format(),
        "ends": this.formatDate(1)
      }
      let datum = Object.keys(payload).map(key => encodeURIComponent(key) + '=' + encodeURIComponent(payload[key])).join('&')

      fetch("http://localhost:8000/api/reservations/",
        {
          method: "POST",
          headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        }
      )
        .then(function (res) { return res.json() })
        .then(function (data) {
          // console.log("FDSA: " + data); 
          // alert(JSON.stringify(data))
          this.setState({
            notification: "We receieved your reservation request"
          })
        })
    }

    return (
      Thing !== undefined &&
      <div style={{ border: '1px solid black', width: 'auto' }}>
        You have chosen {Thing.name}.
      <h1 ref={(input) => { this.MyHONE = input }}>{Thing.name}</h1>
        <p>{Thing.description}</p>
        <p>{Thing.cost_per_hour}</p>
        <p>{Thing.cost_per_day}</p>
        <img className="selected-bike" alt="" src={Thing.image} />
        <Calendar
          notification={this.state.notification}
          onClick={(e) => {
            this.setSelectedDates(e);
          }}
          setSelectedDates={this.setSelectedDates.bind(this)}
          selected={moment().startOf("day")}
          reservations={Thing.reservation_dates} />

        <input id="reserve" type="button" value="Reserve" onClick={function () { submitFormAjax() }} />
      </div>
    )
  }
}