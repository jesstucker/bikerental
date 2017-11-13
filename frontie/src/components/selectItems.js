import React, { Component } from 'react'
import DisplaySelectedItem from './displaySelectedItem';
import axios from 'axios';

export default class SelectItem extends Component {

  componentDidMount() {
    axios.all(["/api/category/?format=json",
      "/api/group/?format=json",
      "/api/item-type/?format=json",
    ].map(api => axios.get(api)))
      .then(axios.spread((req1, req2, req3) => {


        req1.data.unshift({
          "id": -1,
          "description": ""
        })

        this.setState({
          category: req1.data,
          group: req2.data,
          itemType: req3.data
        })
      }))
  }

  state = {
    category: [],
    group: [],
    itemType: [],
    SelectedCategory: null,
    SelectedGroup: null,
    SelectedItem: null
  }

  onChangeCategory = (e) => {
    this.setState({ SelectedCategory: e.target.value });
    this.setState({ SelectedGroup: null });
    this.setState({ SelectedItem: null });
  }

  onChangeGroup = (e) => {
    this.setState({ SelectedGroup: e.target.value });
    this.setState({ SelectedItem: null });
  }

  onChangeItem = (e) => {
    this.setState({ SelectedItem: e.target.value });
  }

  render() {
    var FilteredGroups = [
      {
        "id": -1,
        "description": "",
        "category": "",
        "catg": 0,
        "catg_id": 0
      }
    ]
    for (let i = 0; i < this.state.group.length; i++) {
      var CurrentGroup = this.state.group[i];
      if (CurrentGroup.catg_id == this.state.SelectedCategory) {
        FilteredGroups.push(CurrentGroup)
      }
    }

    var FilteredItems = [
      {
        "id": -1,
        "name": "",
        "group": 0,
        "cost_per_hour": "",
        "cost_per_day": "",
        "image": "",
        "group_id": 0
      }
    ]
    for (let i = 0; i < this.state.itemType.length; i++) {
      var CurrentItem = this.state.itemType[i];
      if (CurrentItem.group_id == this.state.SelectedGroup) {
        FilteredItems.push(CurrentItem)
      }
    }

    let ActuallySelectedItem = this.state.itemType.find(x => x.id == this.state.SelectedItem)
    return (
      <div>
        <select onChange={this.onChangeCategory}>
          {this.state.category.map((catg, i) =>
            <option value={catg.id} key={i}>{catg.description}</option>
          )}
        </select>

        <select onChange={this.onChangeGroup}>
          {FilteredGroups.map((group, i) =>
            <option value={group.id} key={i}>{group.description}</option>
          )}
        </select>

        <select onChange={this.onChangeItem}>
          {FilteredItems.map((item, i) =>
            <option value={item.id} key={i}>{item.name}</option>
          )}
        </select>

        <DisplaySelectedItem ActuallySelectedItem={ActuallySelectedItem} />


      </div>
    )

  }

}