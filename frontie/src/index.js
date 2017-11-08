import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import SelectItem from './components/selectItems';
import Calendar from './components/calendar/Calendar'
import registerServiceWorker from './registerServiceWorker';
import moment from 'moment';






ReactDOM.render(<div>
    <SelectItem />
    <Calendar selected={moment().startOf("day")} />
</div>, document.getElementById('root'));
registerServiceWorker();
