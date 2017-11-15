import React, { Component } from 'react';
import Calendar from './calendar/Calendar';
import moment from 'moment'



export default class DisplaySelectedItem extends Component {
  render() {
    var Thing = this.props.ActuallySelectedItem;
    return (
      Thing !== undefined &&
      <div style={{ border: '1px solid black', width: 'auto' }}>
        You have chosen {Thing.name}.
      <h1>{Thing.name}</h1>
        <p>{Thing.description}</p>
        <p>{Thing.cost_per_hour}</p>
        <p>{Thing.cost_per_day}</p>
        <img className="selected-bike" alt="" src={Thing.image} />
        <Calendar selected={moment().startOf("day")} reservations={Thing.reservation_dates} />
        <form action="#" method="post" name="myform">
          <input type={'hidden'} value={Thing.id} name='id' />
          <input type='submit' value='Reserve' />
        </form>
      </div>
    )
  }
}