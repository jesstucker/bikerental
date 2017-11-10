import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import SelectItem from './components/selectItems';
import registerServiceWorker from './registerServiceWorker';


ReactDOM.render(<div>
    <SelectItem />
</div>, document.getElementById('root'));
registerServiceWorker();