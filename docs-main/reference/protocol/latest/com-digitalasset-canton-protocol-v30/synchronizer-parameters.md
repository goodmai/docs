---
title: "synchronizer_parameters.proto"
description: "Markdown extract for com.digitalasset.canton.protocol.v30 / community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto."
---

# `community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto`

## Navigation

- [Protocol markdown contents](/reference/protocol/latest/contents)
- [Original protobuf package page](/reference/protobuf/packages/com-digitalasset-canton-protocol-v30)
- Package set: `com.digitalasset.canton.protocol.v30` | [com.digitalasset.canton.protocol.v31](/reference/protobuf/packages/com-digitalasset-canton-protocol-v31) | [com.digitalasset.canton.participant.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-participant-protocol-v30) | [com.digitalasset.canton.synchronizer.protocol.v30](/reference/protobuf/packages/com-digitalasset-canton-synchronizer-protocol-v30)
- Source file: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto)

## Related sections in this package

- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/acs_commitments.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/acs-commitments)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/common_stable.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/common-stable)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/confirmation_response.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/confirmation-response)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/mediator.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/mediator)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/merkle.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/merkle)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/ordering_request.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/ordering-request)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_reassignment.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-reassignment)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/participant_transaction.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/participant-transaction)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/quorum.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/quorum)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/sequencing_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/sequencing-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/signed_content.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/signed-content)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/storage.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/storage)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronization.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/synchronization)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/topology)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/traffic_control_parameters.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters)
- [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/versioned_google_rpc_status.proto](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/versioned-google-rpc-status)

## Types in this section

- [com.digitalasset.canton.protocol.v30.AcsCommitmentsCatchUpConfig](#type-com-digitalasset-canton-protocol-v30-acscommitmentscatchupconfig)
- [com.digitalasset.canton.protocol.v30.DynamicSynchronizerParameters](#type-com-digitalasset-canton-protocol-v30-dynamicsynchronizerparameters)
- [com.digitalasset.canton.protocol.v30.ParticipantSynchronizerLimits](#type-com-digitalasset-canton-protocol-v30-participantsynchronizerlimits)
- [com.digitalasset.canton.protocol.v30.OnboardingRestriction](#type-com-digitalasset-canton-protocol-v30-onboardingrestriction)

## Extracted reference

<a id="type-com-digitalasset-canton-protocol-v30-acscommitmentscatchupconfig"></a>
**Message `com.digitalasset.canton.protocol.v30.AcsCommitmentsCatchUpConfig`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto)
- Fields: 2

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| catchup_interval_skip | `uint32` | optional |  |
| nr_intervals_to_trigger_catchup | `uint32` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-dynamicsynchronizerparameters"></a>
**Message `com.digitalasset.canton.protocol.v30.DynamicSynchronizerParameters`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto)
- Fields: 13

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| confirmation_response_timeout | `google.protobuf.Duration` | optional |  |
| mediator_reaction_timeout | `google.protobuf.Duration` | optional |  |
| assignment_exclusivity_timeout | `google.protobuf.Duration` | optional |  |
| ledger_time_record_time_tolerance | `google.protobuf.Duration` | optional |  |
| reconciliation_interval | `google.protobuf.Duration` | optional |  |
| mediator_deduplication_timeout | `google.protobuf.Duration` | optional |  |
| max_request_size | `uint32` | optional |  |
| onboarding_restriction | [`com.digitalasset.canton.protocol.v30.OnboardingRestriction`](#type-com-digitalasset-canton-protocol-v30-onboardingrestriction) | optional |  |
| participant_synchronizer_limits | [`com.digitalasset.canton.protocol.v30.ParticipantSynchronizerLimits`](#type-com-digitalasset-canton-protocol-v30-participantsynchronizerlimits) | optional |  |
| sequencer_aggregate_submission_timeout | `google.protobuf.Duration` | optional |  |
| traffic_control | [`com.digitalasset.canton.protocol.v30.TrafficControlParameters`](/reference/protocol/latest/com-digitalasset-canton-protocol-v30/traffic-control-parameters#type-com-digitalasset-canton-protocol-v30-trafficcontrolparameters) | optional |  |
| acs_commitments_catchup | [`com.digitalasset.canton.protocol.v30.AcsCommitmentsCatchUpConfig`](#type-com-digitalasset-canton-protocol-v30-acscommitmentscatchupconfig) | optional |  |
| preparation_time_record_time_tolerance | `google.protobuf.Duration` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-participantsynchronizerlimits"></a>
**Message `com.digitalasset.canton.protocol.v30.ParticipantSynchronizerLimits`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto)
- Fields: 1

_No description._

| Field | Type | Label | Description |
| --- | --- | --- | --- |
| confirmation_requests_max_rate | `uint32` | optional |  |

<a id="type-com-digitalasset-canton-protocol-v30-onboardingrestriction"></a>
**Enum `com.digitalasset.canton.protocol.v30.OnboardingRestriction`**

- Source: [community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto](https://github.com/DACH-NY/canton/blob/v3.4.11/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto)

_No description._

| Name | Number |
| --- | --- |
| ONBOARDING_RESTRICTION_UNSPECIFIED | `0` |
| ONBOARDING_RESTRICTION_UNRESTRICTED_OPEN | `1` |
| ONBOARDING_RESTRICTION_UNRESTRICTED_LOCKED | `2` |
| ONBOARDING_RESTRICTION_RESTRICTED_OPEN | `3` |
| ONBOARDING_RESTRICTION_RESTRICTED_LOCKED | `4` |
