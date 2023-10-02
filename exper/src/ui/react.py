```python
import React from 'react';
import { investorProfile, experienceSettings, rewardItems, adventureSettings, assistantSettings, invitationDetails, onboardingDetails, realWorldIntegrationSettings, insiderAccessDetails } from '../constants';

class ElysiumApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      investorProfile,
      experienceSettings,
      rewardItems,
      adventureSettings,
      assistantSettings,
      invitationDetails,
      onboardingDetails,
      realWorldIntegrationSettings,
      insiderAccessDetails
    };
  }

  render() {
    return (
      <div className="ElysiumApp">
        <InvestorProfile data={this.state.investorProfile} />
        <ExperienceSettings data={this.state.experienceSettings} />
        <RewardItems data={this.state.rewardItems} />
        <AdventureSettings data={this.state.adventureSettings} />
        <AssistantSettings data={this.state.assistantSettings} />
        <InvitationDetails data={this.state.invitationDetails} />
        <OnboardingDetails data={this.state.onboardingDetails} />
        <RealWorldIntegrationSettings data={this.state.realWorldIntegrationSettings} />
        <InsiderAccessDetails data={this.state.insiderAccessDetails} />
      </div>
    );
  }
}

export default ElysiumApp;
```