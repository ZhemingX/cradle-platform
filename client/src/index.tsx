import 'sanitize.css/sanitize.css';
import './index.css';

import { App } from './app';
import { ConnectedRouter } from 'connected-react-router';
import React from 'react';
import { Provider as ReduxProvider } from 'react-redux';
import { history } from './redux/reducers';
import { reduxStore } from './redux/store';
import { render } from 'react-dom';

render(
  <ReduxProvider store={reduxStore}>
    <ConnectedRouter history={history}>
      <div>
        <App />
      </div>
    </ConnectedRouter>
  </ReduxProvider>,
  document.querySelector(`#root`)
);
