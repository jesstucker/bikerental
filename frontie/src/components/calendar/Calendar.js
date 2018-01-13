import React, { Component } from 'react';
import Week from './Week';
import DayNames from './DayNames';
import moment from 'moment'


export default class Calendar extends Component {

    constructor(props) {
        super(props);
        this.state = {
            month: this.props.selected.clone(),
            selected: this.props.selected,
            dates_selected: [],
            date_picker: [],
            last_selected: null
        }
    };

    toggleReservationSelection = (e) => {
        var el = e.target;
        if (el.classList.contains("not-reserved")) {
            if (el.classList.contains("pending-reserve")) {
                el.classList.remove("pending-reserve")
                this.setState({ dates_selected: this.state.dates_selected.filter(date => date !== el.id) });
                this.props.dates_selected = this.sendDatesSelected();
            } else {
                el.className += " pending-reserve";
                this.setState({ dates_selected: this.state.dates_selected.concat(el.id) });
                this.props.dates_selected = this.sendDatesSelected();
            }

        }
    };



    enumerateBetweenDates = (startDate, endDate) => {
        let dates = [];
        let currDate = moment(startDate).startOf('day');
        let lastDate = moment(endDate).startOf('day');


        while (currDate.add(1, 'days').diff(lastDate) < 0) {
            // console.log(currDate.toDate());
            dates.push(currDate.clone().toDate());
        }
        return dates;
    }



    selectReservationRange = (e) => {
        var el = e.target;
        if (el.classList.contains("not-reserved")) {
            if (this.state.date_picker.length <= 1) {
                el.className += " pending-reserve";
                this.setState({
                    date_picker: this.state.date_picker.concat(el.id),
                    last_selected: el
                })
            }
            if (this.state.date_picker.length >= 2) {
                el.className += " pending-reserve";
                this.state.last_selected.classList.remove("pending-reserve")
                this.setState({
                    date_picker: this.state.date_picker.filter(date => date != this.state.date_picker.slice(-1)).concat(el.id).sort(),
                    last_selected: el
                })

            }
        }
        this.setState({
            dates_selected: this.enumerateBetweenDates(this.state.date_picker[0], this.state.date_picker[1])
        })

    };

    previous = () => {
        var month = this.state.month;
        month.add(-1, "M");
        this.setState({ month: month });
    };

    next = () => {
        var month = this.state.month;
        month.add(1, "M");
        this.setState({ month: month });
    };

    select = (day) => {
        this.setState({ selected: day.date });
        this.forceUpdate();
    };


    renderWeeks = () => {
        var weeks = [],
            done = false,
            date = this.state.month.clone().startOf("month").add("w" - 1).day("Sunday"),
            monthIndex = date.month(),
            count = 0;


        while (!done) {
            weeks.push(<Week key={date.toString()} date={date.clone()}
                month={this.state.month}
                select={this.select}
                selected={this.state.selected}
                reservations={this.props.reservations} />);
            date.add(1, "w");
            done = count++ > 2 && monthIndex !== date.month();
            monthIndex = date.month();
        }
        return weeks;
    };

    renderMonthLabel = () => {
        return <span>{this.state.month.format("MMMM, YYYY")}</span>;
    };

    render() {
        return <div
            style={{ position: 'absolute', right: '0', top: '0' }}
            id="calendar"
            onMouseDown={
                e => {
                    this.selectReservationRange(e);
                    this.props.setSelectedDates(this.state.date_picker);
                }
            }>
            <div className="header">
                <i className="fa fa-angle-left" onClick={this.previous}>&lt;</i>
                {this.renderMonthLabel()}
                <i className="fa fa-angle-right" onClick={this.next}>&gt;</i>
            </div>
            <DayNames />
            {this.renderWeeks()}
            <div>You have selected the following dates: <br />

                {this.state.date_picker.sort()[0]} to {this.state.date_picker.sort()[1]}
                {/* <ul>
                    {this.state.date_picker.map(function (date, index) {
                        return <li key={index}>{date}</li>
                    })}
                </ul> */}
            </div>
        </div>
    }
};