import React, { Component } from 'react';
import axios from 'axios';

export default class Week extends Component {

    constructor(props) {
        super(props);
        this.state = {
            reservations: ['01-01-1970','HEATDEATH'],
        }
    }
    componentDidMount() {
        fetch("api/test/?format=json", {
            method: 'GET',
            headers: {
                Accept: 'application/json',
            },
        })
            .then(response => {
                return response.json()
            })
            .then(response => {
                var dates = [];
                for (var date in response) {
                    dates.push(response[date])
                } return dates;
            })
            .then(dates => {
                this.setState({
                    reservations: dates
                })
            })
    }

    render() {
        var days = [],
            date = this.props.date,
            month = this.props.month,
            resRanges = [];


        var isReserved = (res, date) => res.indexOf(date) > 1 ? 'X' : date


        for (var i = 0; i < 7; i++) {
            var day = {
                name: date.format("dd").substring(0, 1),
                number: date.date(),
                isCurrentMonth: date.month() === month.month(),
                isToday: date.isSame(new Date(), "day"),
                date: date,
            };
            days.push(
                <span
                    key={day.date.toString()}
                    className={"day" + (day.isToday ? " today" : "") +
                        (day.isCurrentMonth ? "" : " different-month") +
                        (day.date.isSame(this.props.selected) ? " selected" : "")}
                    onClick={this.props.select.bind(null, day)}>
              
                    {isReserved(this.state.reservations, day.date.format("MM-DD-YY"))}
                    
                </span>
            );
            date = date.clone();
            date.add(1, "d");


        }

        return <div className="week" key={days[0].toString()}>
            {days}
        </div>
    }
}