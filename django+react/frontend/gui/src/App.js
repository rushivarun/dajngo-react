import React, { Component } from 'react';
import 'antd/dist/antd.css';

import CustomLayout from './containers/layout';
import ArticleList from './containers/article_list_view';

class App extends Component {
  render() {
    return (
      <div className="App">
        <CustomLayout>
          <ArticleList />
        </CustomLayout>
      </div>
    );
  }
}

export default App;
